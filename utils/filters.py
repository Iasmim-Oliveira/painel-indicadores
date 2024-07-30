def aplicar_filtros(filtros):
    # Base da consulta SQL
    base_sql = """
    SELECT
      EXTRACT(MONTH FROM e.dt_minima) AS mes,
      EXTRACT(YEAR FROM e.dt_minima) AS ano,
      SUM(e.area_km2) AS area_influencia_mes,
      COUNT(DISTINCT e.id) AS qtd_eventos,
      SUM(e.qtd_deteccoes) AS qtd_focos
    FROM queimadas.tb_evento AS e
    """

    joins = []
    conditions = []
    
    if 'data_inicio' in filtros and 'data_fim' in filtros:
        conditions.append(f"e.dt_minima >= '{filtros['data_inicio']}'")
        conditions.append(f"e.dt_minima <= '{filtros['data_fim']}'")

    # Adiciona joins e condições de acordo com os filtros
    if 'pais' in filtros and filtros['pais']:
        joins.append("INNER JOIN ibge_bc250_2021.lml_pais_a AS p ON st_intersects(e.geom, p.geom)")
        conditions.append(f"p.sigla = '{filtros['pais']}'")

    if 'uf' in filtros and filtros['uf']:
        joins.append("INNER JOIN bases_auxiliares.ibge_bc250_lim_unidade_federacao_a AS uf ON st_intersects(e.geom, uf.geom)")
        conditions.append(f"uf.nome = '{filtros['uf']}'")
        
    if 'municipio' in filtros and filtros['municipio']:
        joins.append("INNER JOIN bases_auxiliares.ibge_bc250_lim_municipio_a AS mun ON st_intersects(e.geom, mun.geom)")
        conditions.append(f"mun.nome = '{filtros['municipio']}'")
        
    if 'bioma' in filtros and filtros['bioma']:
        biomas_valores = [int(bioma) for bioma in filtros['bioma']]
        joins.append("INNER JOIN queimadas.tb_bioma_subdividida AS b ON st_intersects(e.geom, b.geom)")
        conditions.append(f"b.cd_bioma IN ({', '.join(map(str, biomas_valores))})")

    if 'dominio' in filtros and filtros['dominio']:
        if 'indefinida' in filtros['dominio']:
            joins.append("INNER JOIN dominio.tb_area_nao_identificada AS ni ON st_intersects(e.geom, ni.geom)")
        
        if 'publica' in filtros['dominio']:
            joins.append("INNER JOIN dominio.tb_terra_publica AS tp ON st_intersects(e.geom, tp.geom)")
        
        if 'privada' in filtros['dominio']:
            joins.append("INNER JOIN dominio.tb_terra_privada AS tv ON st_intersects(e.geom, tv.geom)")

    if 'areaEspecial' in filtros and filtros['areaEspecial']:
        if 'is_quilombo' in filtros['areaEspecial']:
            joins.append("INNER JOIN op_incra.tb_area_quilombola AS aq ON st_intersects(e.geom, aq.geom)")
        
        if 'is_terra_indigena' in filtros['areaEspecial']:
            joins.append("INNER JOIN bases_auxiliares.funai_terra_indigena AS ti ON st_intersects(e.geom, ti.geom)")
        
        if 'is_assentamento_federal' in filtros['areaEspecial']:
            joins.append("INNER JOIN op_incra.tb_assentamento_federal AS af ON st_intersects(e.geom, af.geom)")
        
        if 'is_unidade_conservacao' in filtros['areaEspecial']:
            if 'estadual' in filtros['tipoUnidade']:
                joins.append("INNER JOIN  bases_auxiliares.mma_cnuc_unidade_conservacao AS uce ON st_intersects(e.geom, uce.geom)")
                conditions.append("uce.esfera = 'estadual'")

            if 'federal' in filtros['tipoUnidade']:
                joins.append("INNER JOIN  bases_auxiliares.icmbio_unidade_conservacao_federal AS ucf ON st_intersects(e.geom, ucf.geom)")
                conditions.append("ucf.administra = 'Federal'")
    
    
    # Adiciona join para o escopo das queimadas (sempre necessário)
    joins.append("INNER JOIN queimadas.tb_escopo_queimadas AS s ON st_intersects(e.geom, s.geom)")
    
    # Condição fixa
    conditions.append("e.area_km2 > 1")
    conditions.append("e.id_status_evento IN (1, 2, 3)")

    # Constrói a consulta final
    consulta_sql = base_sql + ' ' + ' '.join(joins) + ' WHERE ' + ' AND '.join(conditions) + """
    GROUP BY EXTRACT(MONTH FROM e.dt_minima), EXTRACT(YEAR FROM e.dt_minima)
    ORDER BY EXTRACT(YEAR FROM e.dt_minima), EXTRACT(MONTH FROM e.dt_minima);
    """

    return consulta_sql
