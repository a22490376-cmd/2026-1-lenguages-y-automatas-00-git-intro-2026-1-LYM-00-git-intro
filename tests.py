import os
import pytest
from pathlib import Path
import re


CHECKPOINT_RX = re.compile(r"^- \[([\sxX])\] (.+)$", re.MULTILINE)
GH_REPO_rx = re.compile(r"https://github\.com/[\w-]+/[\w-]+")


def find_checkpoints(file_path: Path) -> dict[str : int | list[str]]:
    """
    Busca todos los checkpoints en un archivo markdown.

    Args:
        file_path: Ruta al archivo markdown

    Returns:
        dict con keys:
            'total': número total de checkpoints
            'completed': número de checkpoints completados
            'incomplete': número de checkpoints incompletos
            'items': lista de tuplas (completado, texto)
    """
    if not os.path.exists(file_path):
        return {"total": 0, "completed": 0, "incomplete": 0, "items": []}

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        return {
            "total": 0,
            "completed": 0,
            "incomplete": 0,
            "items": [f"Error leyendo {file_path}: {e}"],
        }


def _check_checkpoints(md_file: Path):
    with open(md_file, "r", encoding="utf-8") as f:
        content = f.read()
    for m in CHECKPOINT_RX.finditer(content):
        checkpoint_mark = m.group(1)
        checkpoint_txt = m.group(2)

        assert checkpoint_mark.lower() == "x", (
            f"Lección {md_file.name} Falta completar checkpoint: {checkpoint_txt}"
        )


def test_checkpoints_01_instalacion():
    _check_checkpoints(Path("docs/01-INSTALACION.md"))


def test_checkpoints_02_que_es_git():
    _check_checkpoints(Path("docs/02-QUE-ES-GIT.md"))


def test_checkpoints_03_por_que_git():
    _check_checkpoints(Path("docs/03-POR-QUE-GIT.md"))


def test_checkpoints_04_conectar_github():
    _check_checkpoints(Path("docs/04-CONECTAR-GITHUB.md"))


def test_checkpoints_05_comandos_basicos_windows():
    _check_checkpoints(Path("docs/05-COMANDOS-BASICOS-WINDOWS.md"))


def test_checkpoints_06_github_intro():
    _check_checkpoints(Path("docs/06-GITHUB-INTRO.md"))


def test_checkpoints_07_entregables():
    _check_checkpoints(Path("docs/07-ENTREGABLES.md"))


def test_checkpoints_ejercicio():
    _check_checkpoints(Path("docs/EJERCICIO.md"))


def test_assignement():
    tarea = Path("ALUMNO.md")
    assert tarea.exists(), "No se encontró el archivo ALUMNO.md"
    assert tarea.stat().st_size > 0, "El archivo ALUMNO.md está vacío"
    assert tarea.stat().st_size > 30, (
        "El archivo ALUMNO.md es demasiado pequeño (<30 bytes)"
    )
    assert tarea.stat().st_size < 10 * 1024, (
        "El archivo ALUMNO.md es demasiado grande (>10KB)"
    )
    content = tarea.read_text(encoding="utf-8")
    gh_links = GH_REPO_rx.findall(content)
    assert gh_links, "No se encontró ningún enlace de GitHub en ALUMNO.md"
