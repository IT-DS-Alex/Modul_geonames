def similar(question, translate=False, num=5, search=100, names_only=False):
    question = question.lower()
    query = translator.translate(question) if translate else question
    query_embedding = SentenceTransformer('sentence-transformers/LaBSE').encode(query, convert_to_tensor=True, show_progress_bar=False).reshape(1,-1)
    res = util.semantic_search(query_embedding, embeddings, top_k=search)
    idx = [i['corpus_id'] for i in res[0]]
    score = [i['score'] for i in res[0]]
    
    if names_only:
        return (df_filtr.loc[idx].drop_duplicates(subset=['name', 'code']).iloc[:num].name.tolist())
    else:
        return (df_filtr.loc[idx, ['name', 'code', 'name_reg', 'country']]
               .assign(similarity=score)
               .drop_duplicates(subset=['name', 'code'])
               .iloc[:num])