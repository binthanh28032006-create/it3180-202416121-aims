# Changelog

Các thay đổi đáng chú ý của AIMS-mini được ghi trong tệp này.

Định dạng dựa trên [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
phiên bản tuân theo [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [1.1.0] - 2026-11-07
### Added
- `Cart.sort_by_title()` và `Cart.sort_by_cost()`.
- `search_by_category()` để tìm DVD theo thể loại.
### Fixed
- `search_by_title()` không phân biệt hoa thường (Issue #20).

## [1.0.1] - 2026-11-07
### Fixed
- `search_by_title()` không phân biệt hoa thường (Issue #20).

## [1.0.0] - 2026-11-07
### Added
- `Cart.print_cart()` và thông báo riêng khi giỏ rỗng.
- `search_by_title()` để tìm DVD theo tiêu đề.
- `Cart.total_cost_with_discount()` với kiểm tra phần trăm hợp lệ.
- Unit tests cho giỏ hàng và tìm kiếm.
### Fixed
- Giới hạn giỏ hàng: từ chối DVD thứ 21 (Issue #6).

## [0.3.0] - 2026-11-07
### Fixed
- Sửa lỗi giới hạn số lượng DVD trong giỏ hàng.
- Sửa công thức tính tổng tiền sau giảm giá.

## [0.2.0] - 2026-11-07
### Added
- In nội dung giỏ hàng, tìm kiếm DVD theo tiêu đề và tài liệu use case.

## [0.1.0] - 2026-11-07
### Added
- Tổ chức mã nguồn thành package `aims`.
