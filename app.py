from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from Collatz import Collatz_Graph
from Graph_Structure import positioner
from Collatz_Sequence_Graph import GraphMaker
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    """Serve the main HTML page"""
    try:
        return send_from_directory('.', 'index.html')
    except FileNotFoundError:
        return jsonify({'error': 'index.html not found'}), 404

@app.route('/api/generate', methods=['POST'])
def generate_graph():
    """Generate Collatz graph and return HTML directly"""
    try:
        # Validate request has JSON
        if not request.json:
            return jsonify({'error': 'Request must contain JSON data'}), 400
        
        data = request.json
        
        # Validate number exists
        if 'number' not in data:
            return jsonify({'error': 'Missing "number" field'}), 400
        
        try:
            num = int(data['number'])
        except (ValueError, TypeError):
            return jsonify({'error': 'Number must be a valid integer'}), 400
        
        if num < 1 or num > 10000:
            return jsonify({'error': 'Number must be between 1 and 10,000'}), 400
        
        # Generate sequence
        CLG_Nodes = Collatz_Graph(num)
        
        if not CLG_Nodes or len(CLG_Nodes) == 0:
            return jsonify({'error': 'Failed to generate sequence'}), 500
        
        positions = positioner(CLG_Nodes)
        
        # Create graph using GraphMaker
        net = GraphMaker(num, CLG_Nodes, positions)
        
        # Get HTML content directly
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
        print(f"✅ Collatz Visualization Complete!")
        print("="*50)
        print(f"📊 Starting Number: {num}")
        print(f"🔢 Total Steps: {len(CLG_Nodes)}")
        print(f"📈 Peak Value: {max(CLG_Nodes)}")
        print(f"⚡ Growth Factor: {stats['growth_factor']}x")
        print("="*50 + "\n")
        
        # Return HTML + stats
        return jsonify({
            'success': True,
            'html': html_content,
            'stats': stats
        })
        
    except ValueError as e:
        print(f"❌ VALUE ERROR: {str(e)}")
        return jsonify({'error': f'Invalid input: {str(e)}'}), 400
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({'error': 'Internal server error'}), 500


@app.route('/health')
def health():
    return jsonify({
        'status': 'ok',
        'message': 'Collatz Backend Running',
        'version': '1.0.0'
    })


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    
    print("\n" + "="*50)
    print("🚀 Collatz Backend - PRODUCTION MODE")
    print("="*50)
    print(f"🌐 Running on port {port}")
    print("="*50 + "\n")
    
    app.run(host='0.0.0.0', port=port, debug=False)
