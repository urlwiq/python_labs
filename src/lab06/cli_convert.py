import argparse
import sys
import os
from pathlib import Path

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from lab05.json_csv import json_to_csv, csv_to_json
from lab05.csv_xlsx import csv_to_xlsx


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Конвертеры данных (JSON <-> CSV <-> XLSX)",
        epilog="""
Примеры использования:
  python src/lab06/cli_convert.py json2csv --in data/samples/people.json --out data/out/people.csv
  python src/lab06/cli_convert.py csv2json --in data/samples/people.csv --out data/out/people.json
  python src/lab06/cli_convert.py csv2xlsx --in data/samples/people.csv --out data/out/people.xlsx
        """,
    )

    subparsers = parser.add_subparsers(
        dest="command",
        title="Доступные команды",
        description="json2csv - JSON в CSV, csv2json - CSV в JSON, csv2xlsx - CSV в XLSX",
        required=True,
    )

    # json2csv
    p1 = subparsers.add_parser("json2csv", help="Конвертация JSON → CSV")
    p1.add_argument("--in", dest="input", required=True, help="Входной JSON-файл")
    p1.add_argument("--out", dest="output", required=True, help="Выходной CSV-файл")

    # csv2json
    p2 = subparsers.add_parser("csv2json", help="Конвертация CSV → JSON")
    p2.add_argument("--in", dest="input", required=True, help="Входной CSV-файл")
    p2.add_argument("--out", dest="output", required=True, help="Выходной JSON-файл")

    # csv2xlsx
    p3 = subparsers.add_parser("csv2xlsx", help="Конвертация CSV → XLSX")
    p3.add_argument("--in", dest="input", required=True, help="Входной CSV-файл")
    p3.add_argument("--out", dest="output", required=True, help="Выходной XLSX-файл")

    return parser


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    parser = build_parser()

    if not argv or any(arg in argv for arg in ("-h", "--help")):
        parser.print_help()
        return

    args = parser.parse_args(argv)

    # Словарь команд
    command_handlers = {
        "json2csv": json_to_csv,
        "csv2json": csv_to_json,
        "csv2xlsx": csv_to_xlsx,
    }

    try:
        # Проверяем существование входного файла
        if not os.path.exists(args.input):
            raise FileNotFoundError(f"Файл не найден: {args.input}")

        # Создаем директорию для выходного файла
        ensure_directory(args.output)

        # Выполняем команду
        command_handlers[args.command](args.input, args.output)
        print(f"Файл создан: {args.output}")

    except KeyError:
        print("Ошибка: неизвестная команда")
        parser.print_help()
        sys.exit(1)
    except FileNotFoundError as e:
        print(f"Ошибка: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка конвертации: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
