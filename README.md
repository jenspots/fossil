# Fossil

Declarative backup solution for Docker container.

## Example

An example is given below. Every hour, a database dump is created and retrieved to Fossil. Every two hours, the data directory of the database is tar'ed and send to the `s3` endpoint defined in Fossil. We indicate that the database must be brought offline in order to do so with `online=false`. To prevent long downtimes, we also indicate that the database may not be unavailable for more than five seconds.

```yml
version: '3.5'

services:
  postgres:
    # CONTAINER DEFINITION
    labels:
      # General information
      - "fossil.info.enable=true"
      - "fossil.info.name=my-postgres"
      - "fossil.info.max-downtime=5s"

      # Database dump
      - "fossil.dump.interval=3600s"
      - "fossil.dump.command=pg_dump postgres -U postgres"
      - "fossil.dump.destination.local=${TIME}-dump.sql"
      - "fossil.dump.online=true"
      
      # Docker volume backup
      - "fossil.disk.interval=7200s"
      - "fossil.disk.tar=/var/lib/postgresql/data"
      - "fossil.disk.destination.s3=${TIME}-data.tar"
      - "fossil.disk.online=false"
```
