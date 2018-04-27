"""
survey/backend/appserver.py
创建flask实例,启动服务
"""

if __name__ == '__main__':
    from surveyapi.application import create_app
    app = create_app()
    app.run()