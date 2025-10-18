import click

import frappe


def execute():
	frappe_v = frappe.get_attr("frappe" + ".__version__")
	hrms_v = frappe.get_attr("hrms" + ".__version__")

	WIKI_URL = "https://github.com/frappe/hrms/wiki/Changes-to-branching-and-versioning"

	if frappe_v.startswith("14") and hrms_v.startswith("15"):
		message = f"""
			The `develop` branch of Gralab HR is no longer compatible with Gralab & ERPNext's `version-14`.
			Since you are using ERPNext/Gralab `version-14` please switch Gralab HR's branch to `version-14` and then proceed with the update.\n\t
			You can switch the branch by following the steps mentioned here: {WIKI_URL}
		"""
		click.secho(message, fg="red")

		frappe.throw(message)  # nosemgrep
