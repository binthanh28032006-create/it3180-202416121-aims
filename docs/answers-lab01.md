# Câu trả lời thảo luận - Lab 01

## 1. Vì sao dùng `git mv`?

`git mv` thực hiện việc đổi vị trí/đổi tên tệp và cập nhật staging area. Khi xem diff, Git có thể nhận diện đây là thao tác rename dựa trên mức độ tương đồng nội dung, nhờ đó lịch sử của tệp vẫn có thể được tra cứu bằng `git log --follow`. Git không lưu một loại đối tượng rename riêng; rename được nhận diện khi so sánh các snapshot.

## 2. `release/lab01` có phải baseline không?

Có. Nhánh `release/lab01` trỏ tới trạng thái mã nguồn đã thống nhất để nộp Lab 01. Nó là mốc tham chiếu ổn định; thay đổi tiếp theo được phát triển trên `master` hoặc nhánh công việc, không sửa trực tiếp baseline đã nộp.

## 3. Vì sao không commit thẳng lên `master` dù làm một mình?

Nhánh riêng và Pull Request giúp cô lập thay đổi, tạo diff để kiểm tra, lưu lý do thay đổi và thực hành đúng quy trình review. Đây cũng là cách giữ `master` ổn định và có thể áp dụng khi làm nhóm.

## 4. `--global` khác `--local` thế nào?

`--global` lưu cấu hình người dùng trong tệp cấu hình Git ở thư mục home (thường là `~/.gitconfig`) và áp dụng cho các repository của người dùng. `--local` lưu trong `.git/config` của repository hiện tại và chỉ áp dụng cho repo đó; cấu hình local có độ ưu tiên cao hơn global.
