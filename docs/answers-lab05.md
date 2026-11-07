# Câu trả lời thảo luận - Lab 05

## 1. Ưu và nhược điểm của release-first so với upstream-first?

- **Release-first (mô hình bài học):** sửa trực tiếp trên dòng release cũ trước, nên có thể kiểm tra đúng baseline đang gặp lỗi và phát hành patch cho người dùng phiên bản cũ. Sau đó phải lan truyền bản sửa sang `master` và các release khác bằng cherry-pick; nếu quên một dòng phiên bản, lỗi vẫn tồn tại ở dòng đó.
- **Upstream-first:** sửa trên `master` trước để dòng phát triển chính nhận được fix ngay, sau đó cherry-pick sang các release cần bảo trì. Cách này giúp tránh để lỗi tiếp tục đi vào tính năng mới, nhưng cherry-pick sang release cũ có thể cần điều chỉnh do khác biệt mã nguồn.

## 2. Nếu quên lan truyền bản sửa sang `release/lab05`, lệnh nào phát hiện?

Có thể đối chiếu commit cherry-pick và chạy kiểm thử trên từng dòng phiên bản. Một số lệnh kiểm toán:

```bash
git log --all --oneline --grep "cherry picked from commit <FIX_SHA>"
git tag --contains <FIX_SHA>
git cherry -v master release/lab05
```

Ngoài ra, chạy cùng một regression test trên `v1.0.1`, `v1.1.0` và `master`; kết quả mong đợi là đều tìm được `The Lion King` khi từ khóa là `lion`.

## 3. Vì sao commit sửa lỗi và commit nâng phiên bản phải tách riêng?

Commit sửa lỗi chỉ chứa mã sửa và regression test nên có thể cherry-pick sang các dòng phiên bản khác. Commit nâng phiên bản chỉ áp dụng cho dòng release cụ thể; tách riêng giúp không vô tình đưa phiên bản `1.0.1` sang `master` đang ở `1.1.0`.

## 4. Vì sao Issue #20 chỉ tự đóng khi PR vào `master` được merge?

Trong quy trình này, PR hotfix vào `release/lab04` chỉ vá dòng phát hành cũ. PR lan truyền bản sửa vào `master` mới dùng từ khóa đóng Issue (`Fixes #20`), nên việc đóng issue phản ánh lỗi đã được ghi nhận trong dòng phát triển chính.
