# AIMS-mini

Bài thực hành Quản lý cấu hình phần mềm với Git & GitHub - IT3180, HUST.

- Sinh viên: **Nguyễn Hoàng Anh**
- MSSV: **202416121**
- Ngôn ngữ: Python 3.10+
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
.github/                 Pull request template và GitHub Actions
 aims/                   Mã nguồn ứng dụng
 tests/                  Unit tests
 docs/                   Use case, câu trả lời thảo luận, hướng dẫn nộp
 CHANGELOG.md             Lịch sử thay đổi theo Keep a Changelog
 main.py                  Chương trình demo
```

## Các mốc phát hành

| Nhánh | Ý nghĩa |
|---|---|
| `release/lab01` ... `release/lab05` | Baseline nộp từng lab |
| `master` | Dòng phát triển mới nhất |

Các tag phát hành: `v0.1.0`, `v0.2.0`, `v0.3.0`, `v1.0.0`, `v1.0.1`, `v1.1.0`.

Xem [hướng dẫn đưa repository lên GitHub](docs/GITHUB_SETUP.md) trước khi nộp link.
