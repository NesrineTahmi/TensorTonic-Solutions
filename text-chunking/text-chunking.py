def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    # Write code here
    step = chunk_size - overlap
    chunks  = []
    
    if step <= 0 or chunk_size < 1 or len(tokens) < 1:
        return []

    for i in range(0, len(tokens), step):
        chunk = tokens[i : i + chunk_size]
        if (len(chunk) == chunk_size) or ((len(chunk) < chunk_size) and i == 0): 
            chunks.append(chunk)
        
    return chunks
            
            