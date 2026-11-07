# Câu trả lời thảo luận - Lab 04

## 1. Vì sao `release/*` không merge ngược vào `master`?

Nhánh release đại diện cho baseline đã chốt để phát hành/nộp. Phát triển tiếp tục trên `master`; nếu có hotfix cho bản đã phát hành thì sửa trên đúng dòng release rồi lan truyền phần sửa cần thiết sang `master` bằng cherry-pick. Merge ngược cả release có thể kéo theo thay đổi phiên bản hoặc thay đổi chỉ dành riêng cho bản cũ.

## 2. Release Flow trong bài khác GitFlow thế nào?

Release Flow của học phần dùng `master` làm nhánh phát triển chính; feature/topic/bugfix/refactor đi qua PR vào `master`, còn `release/labXX` là baseline riêng cho từng bài. Hotfix được tạo từ nhánh release bị ảnh hưởng rồi đưa về release và master. GitFlow truyền thống thường có thêm nhánh tích hợp dài hạn `develop`, cùng các nhánh `feature`, `release`, `hotfix` xoay quanh `main` và `develop`. Hai mô hình khác nhau ở cách tổ chức nhánh tích hợp và cách phát hành.

## 3. Vì sao phát hành `1.0.0` thay vì `0.4.0`?

Theo SemVer, `0.y.z` biểu thị giai đoạn đầu chưa ổn định. Mốc `1.0.0` đánh dấu baseline đầu tiên được nhóm/học phần coi là bản ổn định để phát hành; nó không đơn thuần là đếm số lab đã hoàn thành.

## 4. Vì sao vừa cần tag vừa cần nhánh release?

Tag annotated định danh một commit chính xác và không di chuyển. Nhánh release có thể tiến lên khi cần áp dụng hotfix. Vì vậy tag trả lời "bản phát hành chính xác là gì", còn nhánh release là dòng bảo trì của bản đó.
