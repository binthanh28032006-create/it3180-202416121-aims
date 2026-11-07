# Hướng dẫn đưa AIMS-mini lên GitHub và nộp bài

Repository dự kiến: `it3180-202416121-aims`.

## 1. Tạo repository rỗng trên GitHub

1. Đăng nhập GitHub và chọn **New repository**.
2. Đặt tên `it3180-202416121-aims`.
3. Chọn **Public** (tài liệu yêu cầu public nếu dùng branch protection với GitHub Free).
4. Không chọn tạo README, `.gitignore` hoặc license vì repository local đã có các tệp này.
5. Tạo repository và sao chép URL SSH hoặc HTTPS.

## 2. Đưa lịch sử, các nhánh và tag lên GitHub

Có thể giải nén file ZIP đi kèm (file này giữ cả thư mục `.git`) hoặc clone từ file bundle. Ví dụ:

```bash
git clone /duong-dan/it3180-202416121-aims.bundle it3180-202416121-aims
cd it3180-202416121-aims
```

Sau đó, thay `<GITHUB_USERNAME>` bằng username GitHub của bạn:

```bash
git remote add origin git@github.com:<GITHUB_USERNAME>/it3180-202416121-aims.git
git push -u origin master
git push origin --all
git push origin --tags
```

Nếu dùng HTTPS, thay URL SSH bằng URL HTTPS GitHub cung cấp. Nếu `origin` đã tồn tại, kiểm tra bằng `git remote -v` và dùng `git remote set-url origin <URL>` thay vì thêm remote lần nữa.

## 3. Kiểm tra sau khi push

```bash
git branch -a
git tag -n
git log --oneline --graph --decorate --all
python -m unittest discover -s tests -v
```

Trên GitHub, kiểm tra các nhánh `release/lab01` đến `release/lab05`, các tag từ `v0.1.0` đến `v1.1.0`, thư mục `aims/`, `tests/`, `docs/` và workflow CI.

## 4. Cấu hình bảo vệ nhánh (nếu được yêu cầu)

Trong **Settings → Branches**, tạo rule cho `master` và `release/*` theo hướng dẫn của lớp:

- Require a pull request before merging.
- Require 1 approval khi có partner; nếu làm một mình, tài liệu cho phép đặt 0 approval.
- Bật dismiss stale approvals nếu được yêu cầu.
- Không cho force push và không cho xóa nhánh release.

Lưu ý: GitHub Free chỉ hỗ trợ branch protection theo điều kiện của tài liệu lớp (repo public; repo private cần quyền lợi phù hợp).

## 5. Những gì cần tự hoàn tất trên giao diện GitHub

Gói repository có lịch sử commit, merge commit cục bộ, nhánh release và tag để bạn kiểm tra. Các thao tác mang tính máy chủ như tạo repository, mở PR, reviewer approval, branch protection và Issue #20 không thể được tạo chỉ bằng cách giải nén gói này. Nếu rubric yêu cầu bằng chứng PR/review/issue trên GitHub, hãy thực hiện các thao tác đó trên repository GitHub thật và không trình bày merge commit cục bộ như một PR đã được GitHub ghi nhận.

## 6. Link nộp

Sau khi push xong, sao chép URL dạng:

`https://github.com/<GITHUB_USERNAME>/it3180-202416121-aims`

Dán URL repository này vào ô nộp bài trên LMS. Không dán link ZIP hoặc link máy tính cá nhân.
