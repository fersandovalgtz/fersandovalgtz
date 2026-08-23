# Estándar común de calidad para repositorios científicos

Este documento define la línea base del ecosistema GitHub de Fernando Sandoval Gutierrez. Su propósito es que cada repositorio alcance una calidad comparable sin borrar las diferencias entre datasets, software de investigación, ediciones histórico-digitales, infraestructura pedagógica y perfil científico.

## Núcleo obligatorio para repositorios de investigación

Cada repositorio debe implementar, cuando corresponda a su naturaleza:

| Dimensión | Evidencia esperada |
|---|---|
| Identidad | nombre estable, versión, tag y descripción inequívoca |
| Citación | `CITATION.cff` con ORCID y versión coherente |
| Metadatos | `codemeta.json` y metadatos de dominio cuando aporten valor |
| Licencia | código, datos y materiales de terceros claramente separados |
| Procedencia | cadena fuente → transformación → producto → release |
| Calidad | reporte, tests, schemas, validadores o invariantes verificables |
| Reproducibilidad | dependencias, scripts, CI y artefactos regenerables |
| Gobernanza | contribución, responsabilidad, límites de autoridad y revisión |
| FAIR / FAIR4RS | autoevaluación conservadora y evidencia enlazable |
| Persistencia | DOI sólo tras depósito real; preservación adicional cuando proceda |
| Documentación | README bilingüe cuando el proyecto tenga proyección internacional |
| Comunicación | estado científico, limitaciones y deuda visible en la portada |
| Seguridad | política de seguridad y mínimo privilegio en workflows |

## Regla epistemológica transversal

La automatización no debe borrar la diferencia entre:

```text
fuente
  ↓
representación de trabajo
  ↓
procesamiento técnico
  ↓
dato derivado
  ↓
validación humana o comunitaria, cuando corresponda
  ↓
interpretación científica
```

Un estado técnico completo no autoriza por sí mismo una afirmación filológica, lingüística, pedagógica, histórica o comunitaria.

## Regla de persistencia

No se inventan DOI, badges de certificación, métricas FAIR, revisiones humanas ni estados de preservación. Un identificador o certificación sólo se muestra cuando puede resolverse y verificarse públicamente.

## Regla visual

La presentación debe ser sobria y científicamente informativa. Los badges deben representar capacidades reales y enlazar, cuando sea posible, a evidencia. La portada debe priorizar propósito, estado, citación, calidad, datos, documentación y limitaciones por encima de decoración o métricas de vanidad.

## Regla de consistencia

Antes de una release se debe comprobar la coherencia entre versión, tag, CFF, CodeMeta, README, changelog, release y DOI. Las referencias cruzadas entre repositorios deben apuntar únicamente a recursos existentes y públicamente accesibles.

## Regla de dominio

El estándar común no obliga a homogeneizar la ciencia. Cada proyecto conserva controles específicos:

- **Rarámuri Digital**: lexicografía, TEI Lex-0, CLDF, API, procedencia documental y validación lingüística/comunitaria diferenciada.
- **Cahíta Histórico Digital**: fuente histórica, transcripción y edición reproducibles, incertidumbre explícita y semántica histórica no modernizada silenciosamente.
- **Rarámuri Histórico**: testimonios históricos, relaciones documentales, IIIF/TEI y separación entre evidencia, propuesta editorial y validación.
- **Libro de Texto Mexicano Digital**: identidad documental, dependencia entre objetos, OCR/segmentación, corpus_ready frente a semantic_ready y análisis histórico posterior.
- **Rarámuri · recursos educativos**: procedencia pedagógica, variación, consentimiento, seguridad cultural y validación situada.

## Mantenimiento

La auditoría de calidad debe repetirse después de una release importante, un cambio de licencia, la incorporación de un DOI, una modificación de contratos de datos o una ampliación sustantiva del alcance científico.
