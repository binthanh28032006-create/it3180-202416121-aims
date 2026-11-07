# AIMS-mini - Use cases

## Tác nhân

* **Khách hàng (Customer):** xem/tìm DVD và xem thông tin giỏ hàng trong bản demo.
* **Nhân viên cửa hàng (Store operator):** thao tác thêm hoặc xóa DVD khỏi giỏ hàng.

## Các ca sử dụng chính

1. **Add DVD to cart:** chọn DVD và thêm vào giỏ nếu giỏ chưa đạt giới hạn 20 đĩa.
2. **Remove DVD from cart:** xóa DVD đã có trong giỏ.
3. **Print cart:** hiển thị nội dung giỏ và tổng tiền; nếu rỗng, hiển thị thông báo riêng.
4. **Calculate total:** tính tổng chi phí các DVD trong giỏ.
5. **Search by title:** tìm DVD theo từ khóa trong tiêu đề.

## Luồng cơ bản - Add DVD to cart

1. Người dùng chọn một DVD.
2. Hệ thống kiểm tra số lượng DVD hiện tại.
3. Nếu còn chỗ, hệ thống thêm DVD và xác nhận; nếu đã đủ 20, hệ thống từ chối.

## Luồng cơ bản - Search by title

1. Người dùng nhập từ khóa.
2. Hệ thống duyệt danh sách DVD.
3. Hệ thống trả về các DVD có tiêu đề chứa từ khóa.

\## Acceptance Criteria



\### Search by title

\- Search must be case-insensitive.

\- An empty keyword returns all DVDs.

\- A matching keyword returns the relevant DVDs.



\### Search by category

\- Search must be case-insensitive.

\- An empty category returns all DVDs.



\### Cart management

\- The cart accepts a maximum of 20 DVDs.

\- The 21st DVD must be rejected.

\- An empty cart displays an appropriate message.

\- The total cost must be calculated correctly.

