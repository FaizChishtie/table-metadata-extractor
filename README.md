# Table Metadata Extractor

Python flask app with an endpoint

## Running Table Metadata Extractor

### Start

```
    sh start.sh
```

The server should start on port 5000

### API

To retrieve table metadata for a database:

Send a POST request to (/) route: 
```
body:
    {
        "uri" : "postgresql://reader:NWDMCE5xdipIjRrp@hh-pgsql-public.ebi.ac.uk:5432/pfmegrnargs"
    }
```

## Todo

- ~~Intial setup~~
- ~~Create route~~
- ~~Connect to SQLAlchemy~~
- ~~Respond with table metadata~~
- Validate route parameters
- Handle errors
- Refactor & clean code

## Commit etiquette

```
chore: add Oyster build script
docs: explain hat wobble
feat: add beta sequence
fix: remove broken confirmation message
refactor: share logic between 4d3d3d3 and flarhgunnstow
style: convert tabs to spaces
test: ensure Tayne retains clothing
```

## Mock DB URI

### Local

```
    sqlite:////{path}/table-metadata-extractor/src/db.sqlite
```

### Public

```
    postgresql://reader:NWDMCE5xdipIjRrp@hh-pgsql-public.ebi.ac.uk:5432/pfmegrnargs
```

[RNAcentral](https://rnacentral.org/help/public-database)
