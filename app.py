from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {
        "name": "顧客管理システム",
        "description": "顧客情報を一元管理するシステムの開発。",
        "client": "ABC株式会社",
        "duration": "6ヶ月",
        "needed_skills": ["Python", "Flask"],
        "team": [
            {"name": "山田一郎", "is_filled": True, "role": "チームリーダー"},
            {"name": "佐藤二郎", "is_filled": False, "role": "開発者"},
            {"name": "鈴木三郎", "is_filled": True, "role": "テスター"},
        ],
    },
    {
        "name": "ECサイト構築",
        "description": "オンラインショッピングサイトの構築。",
        "client": "XYZマーケティング",
        "duration": "3ヶ月",
        "needed_skills": ["JavaScript", "React"],
        "team": [
            {"name": "田中四郎", "is_filled": True, "role": "チームリーダー"},
            {"name": "伊藤五郎", "is_filled": False, "role": "開発者"},
        ],
    },
    {
        "name": "在庫管理システム",
        "description": "リアルタイムで在庫状況を把握するシステムの開発。",
        "client": "オフィスサポート株式会社",
        "duration": "12ヶ月",
        "needed_skills": ["Java", "Spring"],
        "team": [
            {"name": "木村六郎", "is_filled": True, "role": "チームリーダー"},
            {"name": "吉田七郎", "is_filled": True, "role": "デザイナー"},
            {"name": "小林八郎", "is_filled": False, "role": "システムアナリスト"},
        ],
    },
    {
        "name": "モバイルアプリ開発",
        "description": "iOSおよびAndroid向けのモバイルアプリの開発。",
        "client": "アプリクリエイト株式会社",
        "duration": "9ヶ月",
        "needed_skills": ["Swift", "Kotlin"],
        "team": [
            {"name": "佐々木九郎", "is_filled": True, "role": "チームリーダー"},
            {"name": "高橋十郎", "is_filled": False, "role": "開発者"},
            {"name": "遠藤花子", "is_filled": True, "role": "テスター"},
        ],
    },
    {
        "name": "ビッグデータ解析",
        "description": "大量のデータを分析して顧客の行動を予測するシステムの構築。",
        "client": "データサイエンス株式会社",
        "duration": "18ヶ月",
        "needed_skills": ["Python", "Hadoop", "Spark"],
        "team": [
            {"name": "松本一子", "is_filled": True, "role": "チームリーダー"},
            {"name": "中村次郎", "is_filled": True, "role": "データサイエンティスト"},
            {"name": "村田三子", "is_filled": False, "role": "エンジニア"},
        ],
    }
]

@app.route('/')
def index():
    return render_template('index.html', projects=projects)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = projects[project_id]
    return render_template('project_detail.html', project=project)

if __name__ == '__main__':
    app.run(debug=True)