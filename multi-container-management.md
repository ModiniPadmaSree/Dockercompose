This document explains how to manage a multi-container application consisting of: \
Web Service-Flask Python application \
Database Service-PostgreSQL database \
Docker Compose is used to orchestrate and manage both containers together as a single application stack. \
Prerequisites \
1. A ubuntu instance with installed docker and docker compose, git
2. Ensure that specified ports in app are free.
3. A python application with databse integration and docker-compose.yml
Steps to manage mutli-container application usign docker compose
1. Start the application: From the project directory, satrt all services \
  docker compose up -d
2. Verfiy running containers \
docker compose ps
3. Access the application: In browser, ip_of_ec2:port number \
Expected output is python application, here it is "Python Flask App with PostgreSQL is running!"
4. Test database integration: Add and fetch data
Add: curl -X POST http://localhost:5000/add \
-H "Content-Type: application/json" \
-d '{"message": "Docker Compose Test"}' \
Fetch: curl http://localhost:5000/messages
5. Viewing logs: Logs help monitor application behavior and troubleshoot issues. \
To view the logs of services: docker compose logs \
To view the logs of specific service: docker compose logs web \
Follow logs in real time: docker compose logs -f
6. Stop the application: Stops containers but keeps volumes intact. \
docker compose down 
7. Stop and remove everything: Stops container, removes network, database, volumes \
docker compose down -v
8. Restart the service \
docker compose restart \
docker compose restart web(specific service)
9. Scaling application \
docker compose up -d --scale web=3
10. View created networks: docker network ls \
Inspect app network: docker network inspect python-web-app_default \
11. View volumes: docker volume ls 

