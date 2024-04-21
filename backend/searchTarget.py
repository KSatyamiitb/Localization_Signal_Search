import sys
import getSequence as gs

def search_for_sequence(gene_list, gene_amino_acid_sequence):
    targeting_genes = []
    # print(f"{'Gene Name':<{10}} | Target Chain Presence")
    # print("-" * 25)
    for gene_name in gene_list:
        gene = gene_name
        try:
            gene_sequence = gs.getseq([gene])[0][-1]
            # print(f"{gene_name:<{10}} | {gene_amino_acid_sequence in gene_sequence}")
            # print("-" * 25)
            if(gene_amino_acid_sequence in gene_sequence) :
                targeting_genes.append(gene_name)
        except Exception as e:
            continue
    return targeting_genes


if __name__ == "__main__":
    amino_acid_sequence = sys.argv[1]
    # print(amino_acid_sequence)
    gene_list = [substring.strip() for substring in sys.argv[2].split(',')]
    # for gene in gene_list:
    #     print(gene)
    # "IDMLIDLGLDLSD" "SKL" "PKKKRKV"
    targeting_genes = search_for_sequence(gene_list, amino_acid_sequence)
    for gene in targeting_genes:
        print(gene)
    
