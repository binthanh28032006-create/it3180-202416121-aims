# Câu trả lời thảo luận - Lab 03

## 1. Merge base là gì?

Merge base là tổ tiên chung phù hợp của hai nhánh, tức commit mà từ đó hai dòng lịch sử bắt đầu phân kỳ. Khi merge, Git dùng merge base để so sánh thay đổi ở hai phía và xác định vùng có thể tự hợp nhất hoặc gây conflict.

## 2. Vì sao `master` và `release/*` nên dùng `revert` thay vì `reset`?

Đây là các nhánh có lịch sử đã chia sẻ. `reset` di chuyển con trỏ nhánh và có thể viết lại lịch sử mà người khác đã kéo về. `revert` tạo một commit mới đảo ngược tác động của commit cũ, giữ nguyên lịch sử và an toàn hơn cho nhánh dùng chung.

## 3. Vì sao test phải fail trước khi sửa bug?

Một regression test cần tái hiện đúng lỗi trước khi sửa. Nếu test fail trên phiên bản lỗi và pass sau khi sửa, ta có bằng chứng test thực sự phát hiện lỗi và có thể ngăn lỗi quay lại.

## 4. Merge conflict được xử lý thế nào?

Đọc cả hai phiên bản để hiểu ý đồ, sửa tệp thành nội dung kết hợp hợp lý, xóa dấu `<<<<<<<`, `=======`, `>>>>>>>`, chạy test, sau đó `git add` và hoàn tất merge/rebase. Có thể hủy thao tác bằng `git merge --abort` hoặc `git rebase --abort`.
