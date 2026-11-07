def search_by_title(items, keyword):
    """Tìm DVD có tiêu đề chứa keyword (phân biệt hoa thường ở Lab 02)."""
    if not keyword:
        return list(items)
    return [dvd for dvd in items if keyword in dvd.title]
