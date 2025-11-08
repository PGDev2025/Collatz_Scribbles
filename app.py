from flask import Flask, request, jsonify
from flask_cors import CORS
from Collatz import Collatz_Graph
from Graph_Structure import positioner
from Collatz_Sequence_Graph import GraphMaker

app = Flask(__name__)
CORS(app)

@app.route('/api/generate', methods=['POST'])
def generate_graph():
    """Generate Collatz graph and return HTML directly"""
    try:
        data = request.json
        num = int(data.get('number', 0))
        
        if num < 1 or num > 10000:
            return jsonify({'error': 'Number must be between 1 and 10,000'}), 400
        
        # Generate sequence
        CLG_Nodes = Collatz_Graph(num)
        positions = positioner(CLG_Nodes)
        
        # Create graph using GraphMaker
        net = GraphMaker(num, CLG_Nodes, positions)
        
        # Get HTML content directly (NO FILE SAVED!)
        html_content = net.generate_html()
        
        # Calculate stats
        stats = {
            'number': num,
            'steps': len(CLG_Nodes),
            'peak': max(CLG_Nodes),
            'growth_factor': round(max(CLG_Nodes) / num, 2)
        }
        
        # Print stats to console
        print("\n" + "="*50)
        print(f"Collatz Visualization Complete!")
        print("="*50)
        print(f"Starting Number: {num}")
        print(f"Total Steps: {len(CLG_Nodes)}")
        print(f"Peak Value: {max(CLG_Nodes)}")
        print(f"Growth Factor: {stats['growth_factor']}x")
        print("="*50 + "\n")
        
        # Return HTML + stats
        return jsonify({
            'success': True,
            'html': html_content,
            'stats': stats
        })
        
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/health')
def health():
    return jsonify({'status': 'ok', 'message': 'Collatz Backend Running'})


if __name__ == '__main__':
    print("\n" + "="*50)
    print("🚀 Collatz Backend Server - LIVE MODE")
    print("="*50)
    print("📡 API: http://localhost:5000")
    print("🔗 Health: http://localhost:5000/health")
    print("="*50 + "\n")
    
    app.run(debug=True, port=5000, host='0.0.0.0')



