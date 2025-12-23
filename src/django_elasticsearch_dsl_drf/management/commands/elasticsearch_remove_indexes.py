from django.core.management.base import BaseCommand

from ...elasticsearch_helpers import delete_all_indices, get_all_indices


class Command(BaseCommand):
    help = "Remove all indexes from Elasticsearch"

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            "--dry-run",
            action="store_true",
            dest="dry_run",
            default=False,
            help="Dry-run (no db writes)",
        )
        parser.add_argument(
            "--with-protected",
            action="store_true",
            dest="with_protected",
            default=False,
            help="Including protected (for instance, kibana) indexes",
        )

    def handle(self, *args, **options):
        dry_run = options.get("dry_run", False)
        with_protected = options.get("with_protected", False)
        if dry_run:
            indices = get_all_indices(with_protected=with_protected)
            print(f"The following indexes will be removed: {indices}")
        else:
            indices, errors = delete_all_indices(with_protected=with_protected)
            print(f"The following indexes are removed: {indices}")
            print(f"The following indexes could not be removed: {errors}")
