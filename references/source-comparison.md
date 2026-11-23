# Source comparison and evidence

Use this reference for audits, SDK comparisons, request/response inventories, field analyses, or source-backed technology reports.

## Evidence hierarchy

Prefer evidence in this order:

1. Supplied original source code at an identifiable revision.
2. Decompiled class or method tied to an identifiable DEX/APK hash.
3. Manifest, resource, request log, returned object, or runtime record tied to the same sample.
4. Screenshot showing the exact value or UI.
5. Derived explanation using the facts above.

Do not present a derived statement as another source object. Keep the source symbol or field available beside the claim.

## Full-chain reconstruction

Use one ordered chain for every system:

```text
trigger → condition/permission → collection API → normalization → queue/storage → outbound object
```

For each stage, retain:

- entry class and method;
- caller and callee;
- conditions that stop the chain;
- values collected or constructed;
- persistence or de-duplication behavior;
- outbound topic, type, endpoint, and encryption wrapper.

If two systems execute stages in different orders, show that difference in the diagram and code order. Do not hide it inside prose.

## Code comparison

Use identical stage headings for every system. A code card should contain:

- system name;
- source path, class, and method;
- short highlighted excerpt;
- one-sentence explanation of the behavior established by the excerpt.

Highlight statements that show a decisive transition: Message dispatch, API call, permission check, JSON key insertion, queue write, or network action. Do not highlight decorative braces.

When the source is obfuscated, keep the obfuscated symbol and show its meaning through the caller, interface method, field assignment, or string code. A clear mapping looks like:

```text
gbhnm（蓝牙名称请求码）→ D()（蓝牙名称接口）
```

Do not rename a symbol in code if the actual artifact uses another symbol. Put the readable meaning in prose or a trailing comment.

## Field tables

For each field, capture:

| Field | Meaning | Source/API | Nature |
|---|---|---|---|
| `address` | Device address | `BluetoothDevice.getAddress()` | Identifier / key |
| `rssi` | Signal strength | `ScanResult.getRssi()` | Environment signal |

Include serialized order when the order itself is evidence. Mark whether a field is optional, derived, encrypted before send, or grouped with location/network data.

## Sample identity

At the end of the report, include a compact source block with:

- application name and version;
- package name;
- relevant SDK name/version;
- source branch or commit if supplied;
- file or DEX name;
- SHA-256 for the sample and relevant subfile;
- report/topic/endpoint when exposed by source.

Do not mention the capture methodology unless the request is specifically a methodology audit. The report subject is what the SDK or application collected, how it did so, and what data came out.

## Compliance wording

Describe observed behavior first. Connect it to a scenario through concrete facts:

- whether the task is autonomous or user-driven;
- which permissions and configuration gates exist;
- whether nearby devices or only the local adapter are read;
- whether location, cellular, Wi-Fi, battery, or device fingerprint fields share the same record;
- whether data is stored and when it is re-sent;
- whether the outbound value is encrypted.

Avoid claims that a behavior is automatically lawful or unlawful. State the data boundary and the controls the scenario requires.

## Prohibited shortcuts

- Do not infer an API call from a class name alone.
- Do not label a permission irrelevant because the target SDK is old.
- Do not treat an APK hash as proof that every runtime branch executed.
- Do not present class existence as a complete chain.
- Do not say a field is collected if the request object never receives it.
- Do not substitute a generic vendor architecture for the actual sample.
