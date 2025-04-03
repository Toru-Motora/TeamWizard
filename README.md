# Project Manager

Project Managerは、プロジェクトの詳細、メンバー、および人材検索機能を提供するウェブアプリケーションです。

## 特徴
- プロジェクトの詳細表示
- プロジェクトメンバーの表示
- プロジェクトの人材検索およびアサイン

## 使用技術
- Flask (Python)
- HTML
- JavaScript
- D3.js (ビジュアリゼーションライブラリ)
- Bootstrap (CSSフレームワーク)

## セットアップ手順

1. **リポジトリをクローン**

    ```bash
    git clone https://github.com/yourusername/project-manager.git
    cd project-manager
    ```

2. **仮想環境を作成して有効化**

    ```bash
    python -m venv venv
    source venv/bin/activate  # LinuxおよびMacOS
    venv\Scripts\activate  # Windows
    ```

3. **必要なパッケージをインストール**

    ```bash
    pip install -r requirements.txt
    ```

4. **Flaskアプリケーションの環境変数を設定**

    ```bash
    export FLASK_APP=app.py
    export FLASK_ENV=development
    ```

    Windows:
    ```cmd
    set FLASK_APP=app.py
    set FLASK_ENV=development
    ```

5. **アプリケーションの起動**

    ```bash
    flask run
    ```

6. **ブラウザでアクセス**
    ```
    http://127.0.0.1:5000/
    ```

## プロジェクト構成
- team-builder/
  - static/
    - styles.css
  - templates/
    - index.html
    - project_detail.html
  - app.py
  - requirements.txt
  - README.md

## 使用方法

1. **プロジェクト一覧ページ**

    初期表示では、すべてのプロジェクトがリストとして表示されます。各プロジェクト名をクリックすると、プロジェクトの詳細ページに移動します。

2. **プロジェクト詳細ページ**

    選択したプロジェクトの詳細、メンバー一覧、および組織図が表示されます。また、人材検索フォームを使用してプロジェクトに適した人材を検索およびアサインすることができます。

## 貢献方法

1. **リポジトリをフォーク**
2. **機能追加またはバグ修正**
3. **プルリクエストを作成**

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は`LICENSE`ファイルを参照してください。

---

Happy Coding!