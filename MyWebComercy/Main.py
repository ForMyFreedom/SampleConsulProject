import sys
from consul import Consul
from App import app, db

if __name__ == '__main__':
    PORT = sys.argv[1]
    import Routes

    consul = Consul()
    service_name = "mywebcomercy"
    service_id = f'mywebcomercy-{PORT}'

    consul.agent.service.register(
        name=service_name, 
        service_id=service_id, 
        address="127.0.0.1", 
        port=int(PORT), 
        check={
            "http": f'http://127.0.0.1:{PORT}/health',
            "interval": "10s",
            "timeout": "1s"
        }
    )

    with app.app_context():
        db.create_all()
    app.run(port=PORT)