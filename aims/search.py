def search_by_category(items, category):
    """Return DVDs whose category contains the requested text."""
    if not category:
        return list(items)
    category_key = category.casefold()
    return [dvd for dvd in items if category_key in dvd.category.casefold()]


def search_by_title(items, keyword):
    """Tìm DVD có tiêu đề chứa keyword (phân biệt hoa thường trước hotfix)."""
    if not keyword:
        return list(items)
    return [dvd for dvd in items if keyword in dvd.title]
