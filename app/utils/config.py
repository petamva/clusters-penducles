from types import SimpleNamespace

cfg = SimpleNamespace(
    penducles = SimpleNamespace(
        path = './models/penducles_output/model_final.pth',
        metadata = {
            'thing_classes': ['penducle'],
            'thing_dataset_id_to_contiguous_id': {0: 0}
        }
    ),
    clusters = SimpleNamespace(
        path = './models/clusters_output/model_final.pth',
        metadata = {
            'thing_classes': ['cluster'],
            'thing_dataset_id_to_contiguous_id': {0: 0}
        }
    ),
)