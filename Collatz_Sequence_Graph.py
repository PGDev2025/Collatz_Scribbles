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
        bgcolor="#FFFFFF",
        font_color="#1F2937",
        directed=True,
        notebook=False
    )
    
    # ---- Professional modern theme options ----
    net.set_options("""
    {
      "nodes": {
        "borderWidth": 3,
        "borderWidthSelected": 4,
        "size": 35,
        "font": {
          "size": 22,
          "face": "Inter, SF Pro Display, -apple-system, sans-serif",
          "bold": true,
          "color": "#1F2937",
          "vadjust": -50,
          "multi": true
        },
        "shadow": {
          "enabled": true,
          "color": "rgba(0,0,0,0.12)",
          "size": 10,
          "x": 0,
          "y": 3
        }
      },
      "edges": {
        "width": 3,
        "selectionWidth": 1.5,
        "smooth": {
          "enabled": true,
          "type": "cubicBezier",
          "roundness": 0.5
        },
        "arrows": {
          "to": {
            "enabled": true,
            "scaleFactor": 1.2,
            "type": "arrow"
          }
        },
        "shadow": {
          "enabled": true,
          "color": "rgba(0,0,0,0.08)",
          "size": 5,
          "x": 0,
          "y": 2
        }
      },
      "interaction": {
        "hover": true,
        "hoverConnectedEdges": true,
        "tooltipDelay": 100,
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
    
    # ---- Add professional nodes ----
    max_val = max(CLG_Nodes)
    for i, node in enumerate(CLG_Nodes):
        x, y = positions[node]
        
        # Professional light color scheme with high contrast
        if i == 0:  # Starting node - Golden
            color = {
                'background': '#FCD34D',
                'border': '#F59E0B',
                'highlight': {
                    'background': '#FDE68A',
                    'border': '#FBBF24'
                }
            }
            size = 45
            shape = 'dot'
            node_type = 'START'
            border_width = 4
        elif node == 1:  # Goal node - Green star (empty, label below)
            color = {
                'background': '#FFFFFF',
                'border': '#10B981',
                'highlight': {
                    'background': '#F0FDF4',
                    'border': '#22C55E'
                }
            }
            size = 45
            shape = 'star'
            node_type = 'GOAL'
            border_width = 5
        elif node == max_val:  # Peak value - Light Golden
            color = {
                'background': '#FEF3C7',
                'border': '#F59E0B',
                'highlight': {
                    'background': '#FEF9C3',
                    'border': '#FBBF24'
                }
            }
            size = 40
            shape = 'dot'
            node_type = 'PEAK'
            border_width = 4
        elif node % 2 == 0:  # Even numbers - Light Blue
            color = {
                'background': '#DBEAFE',
                'border': '#3B82F6',
                'highlight': {
                    'background': '#EFF6FF',
                    'border': '#60A5FA'
                }
            }
            size = 35
            shape = 'dot'
            node_type = 'EVEN'
            border_width = 3
        else:  # Odd numbers - Light Gray
            color = {
                'background': '#F3F4F6',
                'border': '#6B7280',
                'highlight': {
                    'background': '#F9FAFB',
                    'border': '#9CA3AF'
                }
            }
            size = 35
            shape = 'dot'
            node_type = 'ODD'
            border_width = 3
        
        # Clean professional tooltip
        peak_indicator = ' • PEAK' if node == max_val else ''
        title = f"""
        Node Stats:
        {node}
        Step {i} of {len(CLG_Nodes)-1}
        {node_type}{peak_indicator}
        """
        
        # Format label - for goal node, use custom font to position below
        if node == 1:
            node_label = str(node)
            node_font = {
                'size': 22,
                'face': 'Inter, SF Pro Display, -apple-system, sans-serif',
                'bold': True,
                'color': '#1F2937',
                'vadjust': 70  # Position below star
            }
        else:
            node_label = str(node)
            node_font = {
                'size': 22,
                'face': 'Inter, SF Pro Display, -apple-system, sans-serif',
                'bold': True,
                'color': '#1F2937',
                'vadjust': -50  # Position above
            }
        
        net.add_node(
            node,
            label=node_label,
            x=x,
            y=y,
            physics=False,
            color=color,
            size=size,
            shape=shape,
            title=title,
            borderWidth=border_width,
            font=node_font
        )
    
    # ---- Add professional edges with clear labels ----
    for i in range(len(CLG_Nodes) - 1):
        current = CLG_Nodes[i]
        next_val = CLG_Nodes[i + 1]
        
        if current % 2 == 0:  # Division operation - Dark Blue
            edge_color = {
                'color': '#2563EB',
                'highlight': '#1D4ED8',
                'hover': '#3B82F6'
            }
            edge_label = "n/2"
            dashes = False
        else:  # 3n+1 operation - Dark Red/Orange
            edge_color = {
                'color': '#DC2626',
                'highlight': '#B91C1C',
                'hover': '#EF4444'
            }
            edge_label = "3n+1"
            dashes = False
        
        net.add_edge(
            CLG_Nodes[i], 
            CLG_Nodes[i + 1],
            color=edge_color,
            width=3,
            label=edge_label,
            dashes=dashes,
            font={
                'size': 16, 
                'align': 'middle', 
                'color': '#374151',
                'background': '#FFFFFF',
                'strokeWidth': 0,
                'strokeColor': '#FFFFFF',
                'bold': True,
                'face': 'Inter, sans-serif',
                'vadjust': 0
            },
            labelHighlightBold=True
        )
    
    return net
