# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import getSequence as gs
import json

app = Flask(__name__)
CORS(app)


def search_for_sequence(gene_list, gene_amino_acid_sequence):
    with open('gene_sequence.json', 'r') as file:
        gene_data = json.load(file)
    targeting_genes = []
    # print(f"{'Gene Name':<{10}} | Target Chain Presence")
    # print("-" * 25)
    new_gene_sequence_added = False
    for gene_name in gene_list:
        if gene_name in gene_data:
            if(gene_amino_acid_sequence in gene_data[gene_name]) :
                    targeting_genes.append(gene_name)
        else :
            try:
                gene_sequence = gs.getseq([gene_name])[0][-1]
                # print(f"{gene_name:<{10}} | {gene_amino_acid_sequence in gene_sequence}")
                # print("-" * 25)
                if(gene_amino_acid_sequence in gene_sequence) :
                    targeting_genes.append(gene_name)
                gene_data[gene_name] = gene_sequence
                new_gene_sequence_added = True
            except Exception as e:
                continue
    if new_gene_sequence_added:
        with open('gene_sequence.json', 'w') as file:
            json.dump(gene_data, file, indent=4)
    return targeting_genes


@app.route('/search')
def search():
    query1 = request.args.get('query1')
    query2 = request.args.get('query2')
    print('Search query:', query1, query2)
    amino_acid_sequence = query1
    # print(amino_acid_sequence)
    gene_list = [substring.strip() for substring in query2.split(',')]
    # for gene in gene_list:
    #     print(gene)
    # "IDMLIDLGLDLSD" "SKL" "PKKKRKV"
    targeting_genes = search_for_sequence(gene_list, amino_acid_sequence)
    for gene in targeting_genes:
        print(gene)
    return targeting_genes

if __name__ == '__main__':
    app.run(debug=False, port=5000)


    

