from flask import Flask, render_template, request
from CFG import validate_expression
from Node import CalculatorParser, Node
import graphviz

app = Flask(__name__)
app.secret_key= "secret"


def generate_tree_graph(node):
    """Genera una representación gráfica del árbol sintáctico usando Graphviz."""
    dot = graphviz.Digraph()
    _add_nodes(dot, node)
    return dot

def _add_nodes(dot, node, parent_id=None):
    node_id = str(id(node))
    dot.node(node_id, label=node.value)
    if parent_id:
        dot.edge(parent_id, node_id)
    for child in node.children:
        _add_nodes(dot, child, node_id)

@app.route('/', methods=['GET', 'POST'])
def operar():

    tree_image = None
    expression = ""
    error_message = None    
    result = None

    if request.method == 'POST':
        expression = request.form.get('operation')
        print(expression)

        print(validate_expression(expression))

        parser = CalculatorParser(expression)
        tree = parser.parse()

        if tree:
            try:
                # Evaluar el árbol
                result = tree.evaluate()
                # Generar el gráfico del árbol
                graph = generate_tree_graph(tree)
                graph.render("static/tree", format="png", cleanup=True)
                tree_image = "/static/tree.png"
            except ZeroDivisionError as e:
                error_message = str(e)
            except Exception as e:
                error_message = f"Error al evaluar la expresión: {e}"
        else:   
            error_message = "La expresión es inválida. Inténtalo nuevamente."

                
    return render_template("index.html", tree_image=tree_image, result=result, expression=expression, error_message=error_message)

if __name__=="__main__":
    app.run(debug=True)