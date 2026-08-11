# Ciencia abierta e infraestructura reproducible

[← Volver al perfil](README.md) · [Arquitectura de investigación](RESEARCH.md) · [Producción seleccionada](OUTPUTS.md)

GitHub se utiliza aquí como **infraestructura de investigación**, no como escaparate de programación. El criterio central es que un producto académico digital pueda ser identificado, citado, inspeccionado, versionado, preservado y, cuando corresponda, reutilizado por otras personas y sistemas.

## Del documento al objeto científico digital

La publicación académica convencional conserva un lugar central, pero ciertos problemas de investigación producen materiales que requieren otras formas de circulación: corpus, datasets, vocabularios, esquemas, archivos de metadatos, interfaces de consulta y software. El trabajo de ciencia abierta busca que estos objetos mantengan una relación explícita con sus fuentes, su versión, sus condiciones de uso y sus límites de interpretación.

## Implementación actual: Rarámuri Digital

[Rarámuri Digital](https://github.com/fersandovalgtz/raramuri-digital) constituye el principal caso de implementación. El repositorio articula una infraestructura lexicográfica rarámuri–español con **2,581 entradas** y **30 productos derivados**. La versión de datos 1.0.0 se distribuye en distintos formatos y la plataforma expone servicios de consulta y documentación.

| Dimensión | Implementación |
|---|---|
| **Identificación y cita** | DOI en Zenodo · `CITATION.cff` · ORCID |
| **Preservación** | Software Heritage · control de versiones Git |
| **Interoperabilidad** | CSV · JSON · XML · SQL · TEI Lex-0 · OpenAPI 3.1 |
| **Metadatos** | CodeMeta · metadatos de proyecto · manifiestos |
| **Integridad** | Sumas SHA-256 de exportaciones |
| **Calidad** | Informe reproducible de calidad y validaciones automáticas |
| **Procedencia** | Registro de fuente, documento, páginas y estado de transcripción |
| **Gobernanza** | Política explícita sobre derechos lingüísticos, validación y reutilización |
| **Licenciamiento** | Licencias diferenciadas para código y datos |

## Principios de trabajo

### Trazabilidad antes que apariencia de certeza

Un dato digital debe conservar la posibilidad de volver a su procedencia. Cuando una entrada tiene origen documental, la infraestructura registra esa relación. El hecho de que un recurso pueda consultarse técnicamente no convierte automáticamente su contenido en una afirmación lingüística validada.

### Versionado antes que sustitución silenciosa

Las modificaciones deben quedar asociadas a versiones y cambios identificables. Esto permite distinguir la evolución de los datos, la plataforma y la documentación, y reduce el riesgo de perder el contexto de una corrección.

### Interoperabilidad antes que dependencia de una plataforma

Los datos se publican en formatos diversos para evitar que el valor científico dependa de una única interfaz. TEI Lex-0 permite diálogo con ecosistemas lexicográficos; CSV y JSON facilitan análisis y desarrollo; SQL conserva una representación relacional; OpenAPI documenta acceso programático.

### Cita y preservación como parte del producto

Un proyecto científico digital necesita una forma estable de ser citado y preservado. DOI, CFF, ORCID y Software Heritage cumplen funciones diferentes y complementarias: identificación del producto, atribución, identidad de autor y preservación del estado del software.

### Gobernanza y límites explícitos

La apertura técnica no elimina obligaciones culturales, éticas o jurídicas. En recursos relacionados con lenguas indígenas, la trazabilidad y la licencia deben coexistir con reconocimiento de la autoridad de las comunidades hablantes y con mecanismos de validación y corrección.

## Qué se busca trasladar a futuros productos abiertos

La arquitectura desarrollada para Rarámuri Digital establece un patrón reutilizable para otros productos académicos que lo justifiquen: estructura documental clara, datos separados del código, metadatos legibles por máquina, archivos de citación, control de calidad, identificadores persistentes, exportaciones interoperables y documentación de límites de uso.

No todos los proyectos requieren una API ni todos los materiales deben abrirse. La decisión depende de la naturaleza de las fuentes, los derechos asociados, la sensibilidad de los datos y el beneficio científico real de la publicación.

## Accesos

[Rarámuri Digital](https://raramuri.ceees.mx) · [Repositorio](https://github.com/fersandovalgtz/raramuri-digital) · [Zenodo / DOI](https://doi.org/10.5281/zenodo.21483353) · [OpenAPI](https://raramuri.ceees.mx/api/openapi)

---

La ciencia abierta se entiende en este perfil como una práctica de **responsabilidad documental y técnica**: hacer explícito qué es el producto, de dónde proviene, cómo puede verificarse y bajo qué condiciones puede reutilizarse.