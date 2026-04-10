def pij_aligner(target, query, mode):
    from Bio.Align import PairwiseAligner

    #Validation
    if mode not in ["global","local"]:
        mode = 'global'

    if not target or not query:
        return{"error": "empty sequence provided"}
        
    aligner = PairwiseAligner()
    aligner.mode = mode
    alignment = aligner.align(target, query)

    alignment_list = []
    for aln in alignment:
        alignment_list.append(str(aln))
    best_alignment = alignment[0]
    best_score = best_alignment.score
    aln_range = best_alignment.aligned
    return{
        "best_alignment": str(best_alignment),
        "score": best_score,
        "regions": aln_range,
        "top_alignments": alignment_list
    }

pij_aligner('agctacctaaat', 'agctagctagct', 'global')
