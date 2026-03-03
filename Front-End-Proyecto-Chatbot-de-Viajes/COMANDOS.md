## Paso 0: Vinculación
gcloud init

## Paso 1: Creación del repositorio
gcloud artifacts repositories create repo-crewai-streamlit-frontend --repository-format docker --project ai-engineer-11-inofuente --location us-central1

## Paso 2: Crear la imagen de mi APLICACION y subir al repositorio
gcloud builds submit --config=cloudbuild.yaml --project ai-engineer-11-inofuente

## Paso 3: Comando para despliegue o ejecución de la imagen en el repositorio
gcloud run services replace service.yaml --region us-central1 --project ai-engineer-11-inofuente

## Paso 4: OPCIONAL, Dar permisos de acceso a mi APLICACION. ESTO SE EJECUTA UNA SOLA VEZ
gcloud run services set-iam-policy servicio-itinerario-viajes-kevin-inofuente gcr-service-policy.yaml --region us-central1 --project ai-engineer-11-inofuente


streamlit run app.py