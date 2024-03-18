apiVersion: 2021-10-01
name: usbaDjango
properties:
  containers:
  - name: web-api
    properties:
      image: acrusba.azurecr.io/web-api
      resources:
        requests:
          cpu: 1
          memoryInGb: 1.5
      ports:
        - port: 8001
        
  - name: db
    properties:
      image: postgres:latest
      resources:
        requests:
          cpu: 1
          memoryInGb: 1.5
      ports:
        - port: 5432
      environmentVariables:
        - name: "POSTGRES_USER"
          value: ""
        - name: "POSTGRES_PASSWORD"
          value: ""
        - name: "POSTGRES_DB"
          value: ""
  
  - name: web-django
    properties:
      image: acrusba.azurecr.io/web-django
      resources:
        requests:
          cpu: 2
          memoryInGb: 3
      ports:
        - port: 80
      environmentVariables:
        - name: "POSTGRES_USER"
          value: ""
        - name: "POSTGRES_PASSWORD"
          value: ""
        - name: "POSTGRES_DB"
          value: ""
        - name: "POSTGRES_HOST"
          value: "localhost"
        - name: "POSTGRES_PORT"
          value: "5432"
        - name: "POSTGRES_RDY"
          value: "1"
        - name: "DEBUG"
          value: "0"
        - name: "URL_API"
          value: "http://localhost:8001/"
        - name: "SECRET_KEY"
          value: ""
  osType: Linux
  ipAddress:
    type: Public
    ports:
    - protocol: tcp
      port: 80
  imageRegistryCredentials: # Credentials to pull a private image
  - server: "acrusba.azurecr.io"
    username: ""
    password: ""
type: Microsoft.ContainerInstance/containerGroups