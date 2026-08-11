# Ciencia abierta e infraestructura reproducible

[← Volver al perfil](README.md) · [Arquitectura de investigación](RESEARCH.md) · [Producción seleccionada](OUTPUTS.md)

Utilizo GitHub como **infraestructura de investigación**, no como escaparate de programación. Mi criterio central es que un producto académico digital pueda ser identificado, citado, inspeccionado, versionado, preservado y, cuando corresponda, reutilizado por otras personas y sistemas.

## Del documento al objeto científico digital

La publicación académica convencional conserva un lugar central en mi trabajo, pero ciertos problemas de investigación producen materiales que requieren otras formas de circulación: corpus, datasets, vocabularios, esquemas, archivos de metadatos, interfaces de consulta y software. En mi práctica de ciencia abierta busco que estos objetos mantengan una relación explícita con sus fuentes, su versión, sus condiciones de uso y sus límites de interpretación.

## Implementación actual: Rarámuri Digital

[Rarámuri Digital](https://github.com/fersandovalgtz/raramuri-digital) es mi principal caso de implementación. El repositorio articula una infraestructura lexicográfica rarámuri–español con **2,581 entradas** y **30 productos derivados**. La versión de datos 1.0.0 se distribuye en distintos formatos y la plataforma expone servicios de consulta y documentación.

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

Procuro que todo dato digital conserve la posibilidad de volver a su procedencia. Cuando una entrada tiene origen documental, registro esa relación. El hecho de que un recurso pueda consultarse técnicamente no convierte automáticamente su contenido en una afirmación lingüística validada.

### Versionado antes que sustitución silenciosa

Asocio las modificaciones a versiones y cambios identificables. Esto me permite distinguir la evolución de los datos, la plataforma y la documentación, y reduce el riesgo de perder el contexto de una corrección.

### Interoperabilidad antes que dependencia de una plataforma

Publico los datos en formatos diversos para evitar que su valor científico dependa de una única interfaz. TEI Lex-0 permite diálogo con ecosistemas lexicográficos; CSV y JSON facilitan análisis y desarrollo; SQL conserva una representación relacional; OpenAPI documenta acceso programático.

### Cita y preservación como parte del producto

Considero que un proyecto científico digital necesita una forma estable de ser citado y preservado. DOI, CFF, ORCID y Software Heritage cumplen funciones diferentes y complementarias: identificación del producto, atribución, identidad de autor y preservación del estado del software.

### Gobernanza y límites explícitos

No interpreto la apertura técnica como ausencia de obligaciones culturales, éticas o jurídicas. En recursos relacionados con lenguas indígenas, procuro que la trazabilidad y la licencia coexistan con el reconocimiento de la autoridad de las comunidades hablantes y con mecanismos de validación y corrección.

## Qué quiero trasladar a futuros productos abiertos

La arquitectura que desarrollé para Rarámuri Digital establece un patrón que puedo reutilizar en otros productos académicos cuando tenga sentido: estructura documental clara, datos separados del código, metadatos legibles por máquina, archivos de citación, control de calidad, identificadores persistentes, exportaciones interoperables y documentación de límites de uso.

No todos mis proyectos requieren una API ni todos los materiales deben abrirse. Tomo esa decisión según la naturaleza de las fuentes, los derechos asociados, la sensibilidad de los datos y el beneficio científico real de la publicación.

## Accesos

[Rarámuri Digital](https://raramuri.ceees.mx) · [Repositorio](https://github.com/fersandovalgtz/raramuri-digital) · [Zenodo / DOI](https://doi.org/10.5281/zenodo.21483353) · [OpenAPI](https://raramuri.ceees.mx/api/openapi)

---

Entiendo la ciencia abierta como una práctica de **responsabilidad documental y técnica**: hacer explícito qué es el producto, de dónde proviene, cómo puede verificarse y bajo qué condiciones puede reutilizarse.