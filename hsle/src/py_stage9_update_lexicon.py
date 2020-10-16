from HsleCandidateGenerationUtils import LoadLexiconSet


if __name__=='__main__':

    lexset = LoadLexiconSet(False, None, True)
    print(len(lexset))
    with open('new_lex.txt') as f:
        lines = [l.strip() for l in f.readlines() if len(l.strip())>0]
    lines = [l.split(',') for l in lines]
    lines = [''.join(a.strip().split()) for b in lines for a in b]
    lines = set([l for l in lines if len(l)>0])
    lines = lines.difference(lexset)
    print(len(lines))
    with open('new_lex_clean.txt','w') as f:
        f.write('\n'.join(lines))
