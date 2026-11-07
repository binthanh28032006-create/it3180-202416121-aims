# Câu trả lời thảo luận - Lab 02

## 1. Vì sao phải đồng bộ `master` trước khi tạo/gửi PR?

Nhánh tính năng có thể được tạo từ một phiên bản `master` cũ. Fetch và merge `origin/master` giúp phát hiện xung đột sớm, kiểm tra tính năng trong trạng thái tích hợp mới nhất và làm cho diff của PR phản ánh đúng thay đổi còn thiếu.

## 2. Khi nào không được rebase?

Không rebase các nhánh đã chia sẻ hoặc đang được người khác dựa vào, đặc biệt là `master` và `release/*`. Rebase tạo lại commit với SHA mới, tức là viết lại lịch sử; điều này có thể làm lệch lịch sử của các bản clone khác. Chỉ rebase nhánh riêng chưa chia sẻ.

## 3. `feature/*` khác `topic/*` ra sao?

`feature/*` tập trung vào chức năng sản phẩm có thể nhìn thấy hoặc sử dụng được, ví dụ `feature/search-by-title`. `topic/*` gom một chủ đề hỗ trợ quy trình hoặc tài liệu, ví dụ `topic/pr-template` và `topic/use-case-diagram`. Cả hai đều là nhánh ngắn hạn và được tích hợp qua PR.

## 4. Ba kiểu merge khác nhau thế nào?

- **Merge commit:** giữ các commit trên nhánh và tạo một merge commit thể hiện điểm tích hợp; lịch sử thể hiện nhánh rẽ.
- **Squash and merge:** gộp thay đổi của PR thành một commit trên nhánh đích; lịch sử gọn hơn nhưng mất chuỗi commit riêng lẻ của nhánh.
- **Rebase and merge:** đặt lại các commit của nhánh lên đầu nhánh đích; lịch sử tuyến tính nhưng SHA của commit thay đổi.
