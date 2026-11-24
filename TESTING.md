# Testing Checklist

هذا الملف Checklist فقط. لا يعني أن أي تكامل حي اشتغل.

## Fixtures وهمية للتجربة الورقية

هذه أسماء اختبار فقط، وليست عملاء حقيقيين:

1. `https://example.invalid/alpha-instagram` و`https://example.invalid/alpha-site`
2. `https://example.invalid/beta-instagram` و`https://example.invalid/beta-site`
3. `https://example.invalid/gamma-instagram` و`https://example.invalid/gamma-site`

## الاختبارات المحلية التي تم تشغيلها بعد التصحيح

- تم تشغيل `python3 scripts/validate_repo.py` على كل الملفات المتتبعة.
- تم تشغيل Fixture إيجابي مؤقت خارج الريبو، وكان يجب أن يكتشف Email/Phone/Handle/URL وقيمة Secret وهمية.
- تم تشغيل Fixture سلبي مؤقت خارج الريبو، واحتوى كلمات سياسة وقيمًا فارغة و`example.invalid`، واجتاز الفحص.
- لم يتم اختبار Instagram أو Google Sheets أو Google Docs أو إرسال رسائل.
- لم يتم تشغيل أي Pipeline على بيانات حقيقية.

## شروط النجاح اليدوية

- Lead بدون Instagram ينتقل إلى `MISSING_REQUIRED_DATA`.
- Lead بدون Website ينتقل إلى `MISSING_REQUIRED_DATA`.
- دليل غير قابل للوصول ينتقل إلى `UNVERIFIED` وليس `REJECTED` تلقائيًا.
- كل مسودة تبدأ بحالة `DRAFT`.
- لا تتحول إلى `SENT` إلا بعد تأكيد ياسين للإرسال اليدوي.
- أي Mapping للشيت يعرض للموافقة قبل الكتابة.
