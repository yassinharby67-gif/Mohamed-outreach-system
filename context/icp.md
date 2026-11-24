# ICP and Batch Configuration

## الشرطان الإلزاميان الحاليان

1. وجود حساب Instagram عام.
2. وجود Website يمكن نسبه للشخص أو النشاط.

إذا غاب أحدهما أو لم يمكن التحقق منه، لا يدخل الـLead كمرشح كامل للمرحلة التالية، ويسجل السبب: `ناقص: Instagram` أو `ناقص: Website` أو `غير متحقق منه`.

## Batch Config Template

```yaml
batch_id: "batch-YYYY-MM-DD-001"
target_role: ""
market_or_region: ""
target_count: 0
strict_additional_criteria: []
source_limits: "public sources only"
```

## معايير غير محددة بعد

- ما الأدوار المقبولة في كل Batch؟
- هل الدور أو المنطقة شروط استبعاد صارمة؟
- هل توجد حدود للمتابعين؟ غير محددة.
- ما الحد الأدنى للـProof؟ غير محدد.
- هل يلزم Contact عام بالإضافة إلى Instagram وWebsite؟ غير محدد.
- ما معنى “نتائج كويسة” بشكل قابل للقياس؟ غير محدد.
