# CC-26-27-Personal
El objetivo de este proyecto es desarrollar una aplicación nativa de la nube de apoyo a la decisión para pequeños y medianos agricultores, que combina telemetría de sensores de campo y previsiones meteorológicas para calcular, por parcela, el balance hídrico y la recomendación de riego. La necesidad es clara: la agricultura consume cerca del 70 % del agua dulce extraída en el mundo y, aun así, la mayoría de los productores riega por calendario o por intuición, con datos dispersos que nadie cruza, lo que provoca desperdicio de agua y energía y pérdidas evitables.

Un pequeño productor no puede mantener servidores propios ni un equipo de datos. Necesita un servicio accesible, de pago por uso, que absorba los picos de telemetría y de cálculo del verano o de una noche de helada sin estar sobredimensionado el resto del año. Por eso el problema justifica una solución nativa de la nube.



## Justificación NIST SP 800-145

1. Autoservicio bajo demanda. El productor da de alta su explotación, sus parcelas y sus sensores por sí mismo, sin pedir ayuda a nadie ni esperar a que un técnico lo configure. Esto es clave para pequeños agricultores que no cuentan con personal informático.

2. Acceso amplio a la red. Los datos nacen en el campo y las decisiones se consumen en el campo. Los sensores envían sus lecturas por redes móviles o de largo alcance, y el productor consulta recomendaciones y alertas desde el móvil, la tableta o el ordenador, estés donde estés.

3. Asignación común de recursos. Muchas explotaciones comparten la misma infraestructura, manteniendo sus datos separados y protegidos. Al repartirse el coste entre muchos usuarios, el servicio resulta asequible para explotaciones pequeñas. Además, la información meteorológica de una zona se obtiene una sola vez y se aprovecha para todas las parcelas cercanas.

4. Rápida elasticidad. La demanda no es constante: crece en verano, cuando se riega más y se leen más datos, y se dispara en una noche de helada, cuando hay que calcular riesgos y enviar alertas en pocos minutos. La nube permite aumentar recursos en esos momentos y reducirlos el resto del año, sin pagar por capacidad que no se usa.

5. Servicio medido. El uso se mide y se paga en función de lo consumido, tanto el que hace la aplicación de la infraestructura como el que hace cada productor del servicio (parcelas, sensores, volumen de datos). Esto permite controlar costes, facturar con justicia y mantener el negocio equilibrado.



## Mapeo de Actores NIST SP 500-292

Consumidor:	Productor/gestor de la explotación (consume AgroSense como SaaS). Equipo de desarrollo (consume IaaS/PaaS: cómputo, base de datos gestionada, broker, caché). Usa el servicio y paga por su uso. El equipo, además, elige y configura los recursos cloud
Proveedor. Proveedor cloud público (AWS, Azure, GCP u otro) que ofrece la infraestructura. AgroSense, como proveedor del SaaS hacia el productor. Ofrece, opera y garantiza el servicio según el SLA. Gestiona el aislamiento entre inquilinos
Intermediario (Broker):	Servicios que agregan o median entre consumidor y proveedores: un agregador de datos meteorológicos (que unifica AEMET y Open-Meteo), un revendedor cloud o marketplace, y herramientas de gestión multi-nube/FinOps. Intermediación (añade valor sobre un servicio), agregación (combina varios servicios en uno) y arbitraje (elige el proveedor más conveniente)
Auditor: Entidad certificadora independiente (ISO 27001, ENS) y la autoridad de protección de datos (RGPD). Internamente, los informes de monitorización y de costes. Evalúa de forma independiente la seguridad, la privacidad y el rendimiento de los servicios
Operador: (Carrier)	Operadores de telecomunicaciones que dan conectividad a los sensores (NB-IoT, LTE-M, 4G, LoRaWAN) y acceso a internet al productor. Proporciona la conectividad y el transporte entre consumidores y proveedor


## API Prevista

| Método | Ruta | Descripción | Respuesta |
|---|---|---|---|
| `POST` | `/api/explotaciones` | Crear una explotación | `201` |
| `POST` | `/api/parcelas` | Registrar una parcela | `201` |
| `GET` | `/api/parcelas/{id}` | Consultar una parcela | `200` |
| `POST` | `/api/telemetria` | Enviar lecturas de sensores | `202` |
| `GET` | `/api/parcelas/{id}/balance-hidrico` | Balance hídrico actual | `200` |
| `GET` | `/api/parcelas/{id}/recomendacion` | Cuándo y cuánto regar | `200` |
| `GET` | `/api/alertas` | Listar alertas recibidas | `200` |
| `PUT` | `/api/preferencias-alertas` | Elegir canal y prioridad | `200` |
| `GET` | `/api/parcelas/{id}/historial` | Histórico y consumo de agua | `200` |
| `PUT` | `/api/cultivos/{id}/parametros` | Ajustar coeficientes y umbrales | `200` |


## Diagrama de Arquitetura

<img width="502" height="372" alt="diagrama" src="https://github.com/user-attachments/assets/0445a246-edd6-48c2-8b63-5b1241715f8f" />
