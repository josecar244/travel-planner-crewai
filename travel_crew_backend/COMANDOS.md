## Comando para levantar el endpoint
uvicorn src.travel_crew_backend.main:app --host 127.0.0.1 --port 8005 


docker login


docker buildx build \
  --platform linux/amd64 \
  -t kevininofuentecolque/app-crewai-conversacional-backend-ai-engineer-11:latest \
  --push \
  .


