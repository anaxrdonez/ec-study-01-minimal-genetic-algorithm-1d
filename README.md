# GA mínimo 1D (desde cero)

Proyecto diario #1: implementar un algoritmo genético mínimo para **maximizar** una función en 1D.

## Problema
Maximizar:

f(x) = x * sin(10x) + 1

con x en el rango [0, 1].

## Representación
- Un individuo = un número real `x` en `[0, 1]`.
- Población = array de `pop_size` valores reales.

## Operadores evolutivos
### Selección
- Torneo de tamaño 2:
  - se eligen dos individuos al azar
  - gana el de mayor fitness

### Variación (mutación)
- Mutación gaussiana:
  - x' = x + N(0, sigma)
- Se aplica `clip` para mantener x en `[0, 1]`.

### Reemplazo
- Reemplazo generacional: la descendencia reemplaza a toda la población.

## Cómo ejecutar
Activar el entorno virtual e instalar dependencias:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt