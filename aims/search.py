def search_by_title(items, keyword):
    """Tìm DVD có tiêu đề chứa keyword (phân biệt hoa thường ở Lab 02)."""
    if not keyword:
        return list(items)
    keyword_key = keyword.casefold()
    return [dvd for dvd in items if keyword_key in dvd.title.casefold()]
