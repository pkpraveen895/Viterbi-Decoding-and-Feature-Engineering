import numpy as np

def run_viterbi(emission_scores, trans_scores, start_scores, end_scores):
    """Run the Viterbi algorithm.

    N - number of tokens (length of sentence)
    L - number of labels

    As an input, you are given:
    - Emission scores, as an NxL array
    - Transition scores (Yp -> Yc), as an LxL array
    - Start transition scores (S -> Y), as an Lx1 array
    - End transition scores (Y -> E), as an Lx1 array

    You have to return a tuple (s,y), where:
    - s is the score of the best sequence
    - y is the size N array/seq of integers representing the best sequence.
    """
    L = start_scores.shape[0]
    assert end_scores.shape[0] == L
    assert trans_scores.shape[0] == L
    assert trans_scores.shape[1] == L
    assert emission_scores.shape[1] == L
    N = emission_scores.shape[0]
    
    trans_scores += start_scores
    back_ptrs = np.zeros_like(emission_scores,dtype=np.int32)
    emission_scores += start_scores
    em_scores = np.zeros_like(emission_scores)
    em_scores[0] = start_scores+emission_scores[0]
    
    for k in range(1,N):
        transition_plus_score =trans_scores+np.expand_dims(em_scores[k-1],1)
        back_ptrs[k] =np.argmax(transition_plus_score,0)
        em_scores[k] =np.max(transition_plus_score,0)+emission_scores[k]
    
    v = [np.argmax(end_scores+em_scores[-1])]
    v_score = np.max(end_scores+em_scores[-1])

    for back_ptr in reversed(back_ptrs[1:]):
        v.append(back_ptr[v[-1]])
    v.reverse()
    return v_score,v
