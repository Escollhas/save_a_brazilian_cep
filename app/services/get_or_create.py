def get_or_create_model(session, model, **kwargs):
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return {'model': instance, 'exists': True}
    else:
        instance = model(**kwargs)
        session.add(instance)
        session.commit()
        return {'model': instance, 'exists': False}
