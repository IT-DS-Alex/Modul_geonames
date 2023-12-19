def get_sim(geoname, names=df3.name.drop_duplicates().values, embedding=embedding_model, model=SentenceTransformer('sentence-transformers/LaBSE'), top_k=5):
    result =pd.DataFrame(util.semantic_search(model.encode(geoname), embedding_model, top_k=top_k)[0])
    return result.assign(name=names[result.corpus_id])