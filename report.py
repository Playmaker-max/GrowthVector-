import json, sys
src = sys.argv[1] if len(sys.argv) > 1 else "samples/output_1.json"
d = json.load(open(src))
L = ["# Property Intelligence Report\n"]
L.append("## Summary\n" + d["property_summary"] + "\n")
c = d["listing_copy"]
L.append("## Listing copy\n**" + c["headline"] + "**\n\n" + c["description"] + "\n\n*Social post:* " + c["social_post"] + "\n")
L.append("## Verified facts")
for f in d["verified_facts"]:
    L.append("- " + f["claim"] + " (" + f["confidence"] + ")")
L.append("\n## Missing information")
for m in d["missing_information"]:
    L.append("- " + m)
L.append("\n## Likely buyers")
for b in d["buyer_hypotheses"]:
    L.append("- **" + b["buyer_type"] + "**: " + b["why_it_may_fit"])
L.append("\n## Marketing opportunities")
for o in d["marketing_opportunities"]:
    risk = " _Risk: " + o["risk_or_unknown"] + "_" if o.get("risk_or_unknown") else ""
    L.append("- **" + o["opportunity"] + "**: " + o["reasoning"] + risk)
L.append("\n## Campaign angles")
for a in d["campaign_angles"]:
    L.append("- " + a)
L.append("\n## Compliance warnings")
for w in d["compliance_warnings"]:
    L.append("- " + w)
L.append("\n## Next best action\n" + d["next_best_action"])
out = src.replace(".json", "_report.md")
open(out, "w").write("\n".join(L))
print("wrote", out)
