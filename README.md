# AIMS-mini

Bài thực hành Quản lý cấu hình phần mềm với Git & GitHub - IT3180, HUST.

- Sinh viên: **Nguyễn Hoàng Anh**
- MSSV: **202416121**
- Ngôn ngữ: Python 3.10+
- Phiên bản trên `master`: **1.1.0**
- Phạm vi: Lab 01 đến Lab 05

## Chạy chương trình

```bash
python main.py
```

## Chạy kiểm thử

```bash
python -m unittest discover -s tests -v
```

## Cấu trúc

```text
.github/
  pull_request_template.md
  workflows/ci.yml
aims/
  __init__.py
  cart.py
  dvd.py
  search.py
docs/
  answers-lab01.md ... answers-lab05.md
  use-case.md
  GITHUB_SETUP.md
tests/
  test_cart.py
  test_search.py
  test_search_category.py
CHANGELOG.md
main.py
```

## Các mốc phát hành

| Nhánh | Nội dung |
|---|---|
| `release/lab01` | Refactor package `aims` |
| `release/lab02` | Pull Request template, in giỏ hàng, tìm theo tiêu đề |
| `release/lab03` | Sửa giới hạn giỏ hàng, discount, regression tests |
| `release/lab04` | Baseline `1.0.0`; hotfix `1.0.1` |
| `release/lab05` | Tìm theo thể loại, sắp xếp giỏ hàng, baseline `1.1.0` |
| `master` | Dòng phát triển mới nhất, gồm hotfix và CI |

Các tag annotated: `v0.1.0`, `v0.2.0`, `v0.3.0`, `v1.0.0`, `v1.0.1`, `v1.1.0`.

## Tài liệu

- [Use case](docs/use-case.md)
- [Câu trả lời Lab 01](docs/answers-lab01.md)
- [Câu trả lời Lab 02](docs/answers-lab02.md)
- [Câu trả lời Lab 03](docs/answers-lab03.md)
- [Câu trả lời Lab 04](docs/answers-lab04.md)
- [Câu trả lời Lab 05](docs/answers-lab05.md)
- [Hướng dẫn đẩy repository lên GitHub và nộp bài](docs/GITHUB_SETUP.md)
