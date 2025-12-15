from flask import Flask, request, send_file
import requests
from io import BytesIO

app = Flask(__name__)
xMeRo = "https://freefire.samsedrain.com.np/api/v1/profileboard/"

@app.route('/xProFiLe', methods=['GET'])
def generate_profile():
    try:
        nickname = request.args.get('nickname')
        level = request.args.get('level')
        avatarId = request.args.get('avatarId')
        bannerId = request.args.get('bannerId')
        
        if not all([nickname, level, avatarId, bannerId]):
            return 'Error => To GeT inFo!', 400
        
        profileboard_params = {
            'password': 'K180726733',
            'name': nickname,
            'level': int(level),
            'banner': bannerId,
            'avatar': avatarId
        }
        
        profile_response = requests.get(xMeRo, params=profileboard_params, timeout=30)
        
        if profile_response.status_code != 200:
            return f'Error => To CrEaT ImaGe! (Status: {profile_response.status_code})', 400
        
        img_bytes = BytesIO(profile_response.content)
        
        return send_file(
            img_bytes,
            mimetype='image/png',
            as_attachment=False,
            download_name=f'{nickname}_profile.png'
        )
        
    except requests.exceptions.Timeout:
        return 'Error => TimeOut!', 408
    except Exception:
        return 'Error => SyStEm!', 500

@app.route('/')
def home():
    return 'xProFiLe API Running...', 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
