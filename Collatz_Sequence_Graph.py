#Using pyvis network  directed acyclic graph (Collatz Sequence graph) is created as an html file and displayed in modal
from pyvis.network import Network

def GraphMaker(number, CLG_Nodes, positions):
    """
    Generate styled Collatz graph
    
    Args:
        number (int): Starting number
        CLG_Nodes (list): Collatz sequence nodes
        positions (dict): Node positions from Graph_Structure
    
    Returns:
        Network: PyVis Network object
    """
    
    net = Network(
        height="900px",
        width="100%",
        bgcolor="#f8f9fa",
        font_color="#2c3e50",
        directed=True,
        notebook=False,
        heading=f"Collatz Sequence Journey: {number} -> 1"
    )
    
    # ---- Stylish light theme options ----
    net.set_options("""
    {
      "nodes": {
        "borderWidth": 4,
        "borderWidthSelected": 6,
        "size": 28,
        "font": {
          "size": 18,
          "face": "Inter, system-ui, sans-serif",
          "bold": true,
          "color": "#2c3e50"
        },
        "shadow": {
          "enabled": true,
          "color": "rgba(0,0,0,0.15)",
          "size": 15,
          "x": 4,
          "y": 4
        },
        "shapeProperties": {
          "borderRadius": 6
        }
      },
      "edges": {
        "width": 4,
        "selectionWidth": 2,
        "color": {
          "color": "#95a5a6",
          "highlight": "#3498db",
          "hover": "#e74c3c"
        },
        "smooth": {
          "enabled": true,
          "type": "cubicBezier",
          "roundness": 0.6
        },
        "arrows": {
          "to": {
            "enabled": true,
            "scaleFactor": 1.5,
            "type": "arrow"
          }
        },
        "shadow": {
          "enabled": true,
          "color": "rgba(0,0,0,0.1)",
          "size": 8,
          "x": 2,
          "y": 2
        }
      },
      "interaction": {
        "hover": true,
        "hoverConnectedEdges": true,
        "tooltipDelay": 50,
        "zoomView": true,
        "dragView": true,
        "navigationButtons": true,
        "keyboard": {
          "enabled": true,
          "speed": {
            "x": 10,
            "y": 10,
            "zoom": 0.02
          }
        }
      },
      "physics": {
        "enabled": false
      }
    }
    """)
    
    # ---- Add stylish nodes ----
    max_val = max(CLG_Nodes)
    for i, node in enumerate(CLG_Nodes):
        x, y = positions[node]
        
        # Elegant color palette
        if node == CLG_Nodes[0]:  # Starting node
            color = {
                'background': '#e74c3c',
                'border': '#c0392b',
                'highlight': {
                    'background': '#ff6b6b',
                    'border': '#e74c3c'
                }
            }
            size = 40
            shape = 'diamond'
            node_type = 'START'
        elif node == 1:  # Ending node
            color = {
                'background': '#27ae60',
                'border': '#229954',
                'highlight': {
                    'background': '#2ecc71',
                    'border': '#27ae60'
                }
            }
            size = 40
            shape = 'star'
            node_type = 'END'
        elif node == max_val:  # Peak value
            color = {
                'background': '#f39c12',
                'border': '#d68910',
                'highlight': {
                    'background': '#f1c40f',
                    'border': '#f39c12'
                }
            }
            size = 35
            shape = 'dot'
            node_type = 'PEAK'
        elif node % 2 == 0:  # Even numbers
            color = {
                'background': '#3498db',
                'border': '#2980b9',
                'highlight': {
                    'background': '#5dade2',
                    'border': '#3498db'
                }
            }
            size = 28
            shape = 'dot'
            node_type = 'EVEN'
        else:  # Odd numbers
            color = {
                'background': '#9b59b6',
                'border': '#8e44ad',
                'highlight': {
                    'background': '#bb8fce',
                    'border': '#9b59b6'
                }
            }
            size = 28
            shape = 'dot'
            node_type = 'ODD'
        
        # Rich tooltip without emojis
        peak_badge = 'PEAK VALUE!' if node == max_val else 'NOT PEAK VALUE!'
        title = f"""
                Node value:{node}
                Step: {i} of {len(CLG_Nodes)-1}
                Type:{node_type}
                {peak_badge}
        """
        
        net.add_node(
            node,
            label=str(node),
            x=x,
            y=y,
            physics=False,
            color=color,
            size=size,
            shape=shape,
            title=title
        )
    
    # ---- Add elegant edges ----
    for i in range(len(CLG_Nodes) - 1):
        current = CLG_Nodes[i]
        next_val = CLG_Nodes[i + 1]
        
        if current % 2 == 0:  # Division operation
            edge_color = {
                'color': '#3498db',
                'highlight': '#2980b9',
                'hover': '#5dade2'
            }
            edge_label = "/ 2"
            dashes = False
        else:  # 3n+1 operation
            edge_color = {
                'color': '#e74c3c',
                'highlight': '#c0392b',
                'hover': '#ff6b6b'
            }
            edge_label = "3n + 1"
            dashes = [5, 5]
        
        net.add_edge(
            CLG_Nodes[i], 
            CLG_Nodes[i + 1],
            color=edge_color,
            width=4,
            label=edge_label,
            dashes=dashes,
            font={
                'size': 14, 
                'align': 'middle', 
                'color': '#2c3e50',
                'background': 'rgba(255,255,255,0.9)',
                'strokeWidth': 0
            }
        )
    
    return net